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
- **Action Segments:** 83
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 1
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 3
- **Missing Segments:** 2
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
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
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `16` | `15` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `17` | `16` |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 12 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 12 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 12 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 12 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 12 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 12 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 12 | 38 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `14` | `13` | 62 | START | 85 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `1` | `0` | 65 | START | 65 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `2` | `1` | 65 | START | 65 | 79 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `4` | `3` | 65 | START | 65 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `7` | `6` | 65 | START | 65 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `8` | `7` | 65 | START | 69 | 82 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `16` | `15` | 77 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `16` | `15` | 82 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | Position_Unknown | `17` | `16` | 90 | START | 116 | 156 |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | `16` | `15` | 97 | START | 112 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `21` | `19` | 109 | START | 148 | 157 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 156 | BOUNDARY | N/A | N/A |

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
| `Action_PreSnap` | 42 | 45 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 61 | 7 | inferred_complete_timeline |
| `Action_None` | 62 | 210 | 149 | inferred_complete_timeline |

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
| `Action_PreSnap` | 12 | 61 | 50 | inferred_complete_timeline |
| `Action_None` | 62 | 70 | 9 | inferred_complete_timeline |
| `Action_None` | 72 | 76 | 5 | inferred_complete_timeline |
| `Action_None` | 85 | 101 | 17 | inferred_complete_timeline |
| `Action_None` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 125 | 9 | inferred_complete_timeline |
| `Action_None` | 127 | 134 | 8 | inferred_complete_timeline |

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
| `Action_PreSnap` | 12 | 64 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 79 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 101 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 106 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 113 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 124 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 127 | 156 | 30 | inferred_complete_timeline |
| `Action_None` | 157 | 200 | 44 | inferred_complete_timeline |
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
| `Action_PreSnap` | 12 | 64 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 91 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 104 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 112 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 136 | 23 | inferred_complete_timeline |
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
| `Action_PreSnap` | 12 | 64 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 82 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 101 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 156 | 53 | inferred_complete_timeline |
| `Action_None` | 157 | 210 | 54 | inferred_complete_timeline |

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
| `Action_PreSnap` | 12 | 64 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 80 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 85 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 141 | 52 | inferred_complete_timeline |
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
| `Action_PreSnap` | 12 | 64 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 70 | 6 | inferred_complete_timeline |

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
| `Action_PreSnap` | 12 | 61 | 50 | inferred_complete_timeline |
| `Action_None` | 62 | 91 | 30 | inferred_complete_timeline |
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
| `Action_PreSnap` | 12 | 61 | 50 | inferred_complete_timeline |
| `Action_None` | 62 | 170 | 109 | inferred_complete_timeline |
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
| `Action_PreSnap` | 12 | 44 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 61 | 8 | inferred_complete_timeline |
| `Action_None` | 62 | 65 | 4 | inferred_complete_timeline |
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
| `Action_PreSnap` | 12 | 61 | 50 | inferred_complete_timeline |
| `Action_None` | 62 | 96 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 71–108 | 33 | 4 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 78–142 | 64 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 85–210 | 114 | 3 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 85–210 | 126 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 112–135 | 22 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 116–210 | 95 | 2 | Undefined position; Undefined team |
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

- ⚠️ `Action_BallSnap` for actor_track_id `14` (Position_Unknown): Annotated start 62 != Inferred start 85
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (11 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (7 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (3 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `16` (Position_Unknown)
- ❌ Missing segment for action `Action_ReadDefender` on target `16` (Position_Unknown)
- ⚠️ `Action_BlockSecondLevel` for actor_track_id `17` (Position_Unknown): Annotated start 90 != Inferred start 116
- ⚠️ `Action_Handoff` for actor_track_id `16` (Position_Unknown): Annotated start 97 != Inferred start 112
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 8 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '0' (LG) duration 92 frames exceeds threshold 90 frames [start=65, end=156].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (LT) duration 92 frames exceeds threshold 90 frames [start=65, end=156].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (RG) duration 92 frames exceeds threshold 90 frames [start=65, end=156].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (C) duration 92 frames exceeds threshold 90 frames [start=65, end=156].
- ⚠️ Segment 'Action_BallSnap' for track '13' has invalid range: start=85, end=77. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '15' has invalid range: start=112, end=77. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '15' has invalid range: start=112, end=96. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '15' has invalid range: start=112, end=108. Clamping end to start.
- ⚠️ Action 'Action_ZoneBlock' range [65-91] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-104] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-112] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [114-136] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-79] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-90] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-101] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-106] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-113] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-124] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-200] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-170] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-70] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-91] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-111] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-96] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-80] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-85] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-141] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-171] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-64] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-82] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-101] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-38] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-45] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-210] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-70] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-76] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-101] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-125] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-134] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-44] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-105] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-138] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-104] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-210] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [116-156] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-193] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-166] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [148-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [165-178] for track '19' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_189'; source metadata written as null.

</details>