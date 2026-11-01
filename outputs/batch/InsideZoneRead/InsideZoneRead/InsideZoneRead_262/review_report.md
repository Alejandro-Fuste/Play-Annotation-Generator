# Play-Annotation-Generator Annotation Review — InsideZoneRead_262

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_262`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 124
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | DT1 | defense | `13` | `12` |
| ✅ EXACT | `Action_ReadDefender` | DT1 | defense | `13` | `12` |
| ✅ EXACT | `Action_Keep` | DT1 | defense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT1 | defense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 10 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `20` | `16` | 11 | START | 68 | 68 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `0` | 14 | START | 14 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `9` | 14 | START | 14 | 26 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `11` | `10` | 14 | START | 14 | 23 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `5` | `4` | 14 | START | 14 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `6` | `5` | 14 | START | 14 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | DT1 | `13` | `12` | 25 | END | 11 | 14 |
| ✅ EXACT | `Action_ReadDefender` | DT1 | `13` | `12` | 30 | START | 30 | 36 |
| ✅ EXACT | `Action_Keep` | DT1 | `13` | `12` | 37 | START | 37 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT1 | `13` | `12` | 61 | START | 125 | 126 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 84 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 29 | 19 | inferred_complete_timeline |
| `Action_None` | 31 | 86 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–51
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 51 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 26 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 59 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 84 | 24 | inferred_complete_timeline |
| `Action_None` | 85 | 101 | 17 | inferred_complete_timeline |
| `Action_None` | 109 | 110 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 59 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 70 | 3 | inferred_complete_timeline |
| `Action_None` | 85 | 117 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–23
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 23 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 84 | 71 | inferred_complete_timeline |
| `Action_None` | 85 | 140 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 64 | 54 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 2–210
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 10 | 9 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 14 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 18 | 25 | 8 | inferred_complete_timeline |
| `Action_None` | 26 | 29 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 30 | 36 | 7 | inferred_complete_timeline |
| `Action_Keep` | 37 | 60 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 128 | 133 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 141 | 210 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 58 | 48 | inferred_complete_timeline |
| `Action_None` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_None` | 73 | 125 | 53 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 111 | 101 | inferred_complete_timeline |
| `Action_None` | 130 | 155 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 109 | 99 | inferred_complete_timeline |
| `Action_None` | 122 | 128 | 7 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–51
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 10 | 2 | inferred_complete_timeline |
| `Action_None` | 11 | 12 | 2 | inferred_complete_timeline |
| `Action_None` | 15 | 36 | 22 | inferred_complete_timeline |
| `Action_None` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_None` | 45 | 51 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–137 | 102 | 7 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 18–71 | 46 | 3 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 43–106 | 55 | 4 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 51–133 | 82 | 2 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 68–69 | 2 | 2 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 69–210 | 136 | 3 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 70–107 | 38 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 73–210 | 138 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 74–148 | 72 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 77–205 | 95 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 83–131 | 49 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 88–121 | 33 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 111–132 | 22 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 120–145 | 26 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 129–169 | 41 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 131–210 | 79 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 134–210 | 72 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 134–135 | 2 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 135–210 | 76 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 155–201 | 31 | 2 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 180–207 | 28 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `20` (Position_Unknown): Annotated start 11 != Inferred start 68
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 524: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 524: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '16' has invalid range: start=68, end=25. Clamping end to start.
- ⚠️ Action 'Action_None' range [85-140] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-111] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-155] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-42] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-58] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-84] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-105] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-120] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-137] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-109] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-128] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [14-51] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [14-59] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-70] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-58] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-125] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-64] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-29] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-86] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [14-26] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-59] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [14-23] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-12] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-36] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-40] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-51] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' for track '12' starts at frame 11, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_SnapReceive' range [11-14] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [37-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [125-126] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [128-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [141-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-59] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-83] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-99] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-133] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 69, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [69-69] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-197] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-107] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-210] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-131] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-148] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-189] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-205] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-131] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-94] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-121] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-132] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-145] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-171] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-138] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-183] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-207] for track '32' has 5 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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