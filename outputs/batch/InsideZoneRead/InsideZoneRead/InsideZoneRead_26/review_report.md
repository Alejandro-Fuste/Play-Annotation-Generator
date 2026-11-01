# Play-Annotation-Generator Annotation Review — InsideZoneRead_26

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_26`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 22
- **Ball Tracks:** 1
- **Action Segments:** 66
- **Validation Warnings:** 76
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 45
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `6` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 35 |
| ✅ EXACT | `Action_BallSnap` | C | `6` | `5` | 36 | START | 36 | 50 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `10` | `9` | 38 | START | 38 | 105 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 38 | START | 38 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `3` | 38 | START | 38 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `4` | 38 | START | 38 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `6` | `5` | 38 | START | 51 | 54 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 50 | END | 36 | 50 |
| ✅ EXACT | `Action_ReadDefender` | QB | `8` | `7` | 51 | START | 51 | 65 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `7` | 66 | START | 66 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `6` | 77 | START | 97 | 118 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 105 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_SnapReceive` | 36 | 50 | 15 | inferred_complete_timeline |
| `Action_ReadDefender` | 51 | 65 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 66 | 71 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 72 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 97 | 118 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 121 | 127 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 133 | 150 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 105 | 68 | inferred_complete_timeline |
| `Action_None` | 107 | 118 | 12 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_None` | 131 | 150 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 105 | 68 | inferred_complete_timeline |
| `Action_None` | 106 | 150 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_BallSnap` | 36 | 50 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 54 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 73 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_None` | 120 | 123 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 50 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 67 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 105 | 27 | inferred_complete_timeline |
| `Action_None` | 106 | 115 | 10 | inferred_complete_timeline |
| `Action_None` | 122 | 150 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 85 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 105 | 17 | inferred_complete_timeline |
| `Action_None` | 106 | 149 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 150 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 60 | 25 | inferred_complete_timeline |
| `Action_None` | 87 | 89 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 65 | 30 | inferred_complete_timeline |
| `Action_None` | 68 | 70 | 3 | inferred_complete_timeline |
| `Action_None` | 93 | 150 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 98 | 63 | inferred_complete_timeline |
| `Action_None` | 106 | 121 | 16 | inferred_complete_timeline |
| `Action_None` | 123 | 150 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `13` | Position_Unknown | Team_Unknown | 55–117 | 52 | 3 | Undefined position; Undefined team |
| `13` | `16` | Position_Unknown | Team_Unknown | 73–112 | 40 | 1 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 79–150 | 71 | 2 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 96–107 | 9 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 100–134 | 32 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 109–150 | 42 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 121–150 | 30 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 122–150 | 29 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 134–150 | 17 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 141–150 | 9 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 142–150 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `12` | `14` | 58 | 62 | 5 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (4 segments found)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [36–50], lower_priority='Action_ZoneBlock' annotated_start=38, effective_Action_ZoneBlock_start=51.
- ⚠️ Action 'Action_None' range [36-65] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-70] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-150] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-105] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-118] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-150] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-60] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-50] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-53] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-67] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-115] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-85] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-105] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-149] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-54] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-64] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-73] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-97] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-72] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [97-118] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [121-127] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [130-131] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [133-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [66-71] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-98] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-121] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-150] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-79] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-109] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-112] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-103] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-101] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-117] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-134] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-145] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>