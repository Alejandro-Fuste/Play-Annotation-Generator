# Play-Annotation-Generator Annotation Review — InsideZoneRead_189

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_189`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `8` | `7` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 12 | START | 12 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 12 | START | 12 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 12 | START | 12 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 12 | START | 12 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 12 | START | 12 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 12 | START | 12 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 12 | START | 12 | 38 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `7` | 39 | START | 39 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `1` | `0` | 42 | START | 42 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `2` | `1` | 42 | START | 42 | 79 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `4` | `3` | 42 | START | 42 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `7` | `6` | 42 | START | 42 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `8` | `7` | 42 | START | 52 | 64 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `9` | `8` | 51 | END | 42 | 45 |
| ✅ EXACT | `Action_ReadDefender` | QB | `9` | `8` | 56 | START | 56 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `7` | `6` | 65 | START | 65 | 80 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `8` | 71 | START | 71 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `10` | `9` | 83 | START | 85 | 101 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 125 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 12–210
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 42 | 45 | 4 | inferred_complete_timeline |
| `Action_None` | 55 | 55 | 1 | inferred_complete_timeline |
| `Action_ReadDefender` | 56 | 70 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 71 | 82 | 12 | inferred_complete_timeline |
| `Action_None` | 83 | 210 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 12–134
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 70 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 76 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 85 | 101 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 117 | 125 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 127 | 134 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 12–207
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 41 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 79 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 101 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 106 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 113 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 124 | 7 | inferred_complete_timeline |
| `Action_None` | 127 | 200 | 74 | inferred_complete_timeline |
| `Action_None` | 203 | 207 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 12–194
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 41 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 91 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 104 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 112 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 125 | 12 | inferred_complete_timeline |
| `Action_None` | 126 | 136 | 11 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 12–210
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_BallSnap` | 39 | 51 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 64 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 82 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 101 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 125 | 22 | inferred_complete_timeline |
| `Action_None` | 126 | 210 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 12–210
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 41 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 64 | 23 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 65 | 80 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 82 | 85 | 4 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 90 | 125 | 36 | inferred_complete_timeline |
| `Action_None` | 126 | 141 | 16 | inferred_complete_timeline |
| `Action_None` | 163 | 171 | 9 | inferred_complete_timeline |
| `Action_None` | 173 | 210 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 12–70
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 41 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 70 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 12–121
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_None` | 39 | 91 | 53 | inferred_complete_timeline |
| `Action_None` | 93 | 111 | 19 | inferred_complete_timeline |
| `Action_None` | 118 | 121 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 12–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_None` | 39 | 170 | 132 | inferred_complete_timeline |
| `Action_None` | 177 | 210 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 12–82
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_None` | 39 | 44 | 6 | inferred_complete_timeline |
| `Action_None` | 54 | 65 | 12 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_None` | 70 | 82 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 12–96
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 38 | 27 | inferred_complete_timeline |
| `Action_None` | 39 | 96 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 71–108 | 33 | 4 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 78–142 | 64 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 85–210 | 114 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 85–210 | 126 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 112–135 | 22 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 116–210 | 95 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 126–193 | 68 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 133–169 | 36 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 148–178 | 24 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 158–208 | 32 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 163–210 | 48 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 169–210 | 42 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 196–207 | 12 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 203–210 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (10 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (5 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [39–51], lower_priority='Action_ZoneBlock' annotated_start=42, effective_Action_ZoneBlock_start=52.
- ⚠️ Action 'Action_ZoneBlock' range [42-91] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-104] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-112] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-136] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [42-79] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-90] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-101] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-106] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-113] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-124] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-200] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-170] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [42-70] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-91] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-111] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-96] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [65-80] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [82-85] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-141] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-171] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-64] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-82] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-101] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-38] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [42-45] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-210] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-70] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-76] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [85-101] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [106-109] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [113-114] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [117-125] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [127-134] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-44] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-105] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-138] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-104] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-210] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-118] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-193] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-166] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-178] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-186] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-207] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '24' has 1 frames without a visible bounding box.
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