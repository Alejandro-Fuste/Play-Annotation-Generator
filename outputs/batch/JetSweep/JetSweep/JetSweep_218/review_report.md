# Play-Annotation-Generator Annotation Review — JetSweep_218

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_218`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `14` | `13` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `6` |
| ⚠️ START CHANGED | `Action_LeadBlock` | Position_Unknown | Team_Unknown | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Toss` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `16` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `14` | `13` | 27 | START | 28 | 44 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `6` | 37 | START | 37 | 44 |
| ⚠️ START CHANGED | `Action_LeadBlock` | Position_Unknown | `15` | `14` | 38 | START | 40 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `10` | `9` | 38 | START | 38 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `4` | `3` | 38 | START | 38 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `6` | `5` | 38 | START | 38 | 47 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `7` | `6` | 38 | START | 52 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `8` | 38 | START | 38 | 61 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 50 | END | 43 | 50 |
| ✅ EXACT | `Action_Toss` | QB | `16` | `15` | 54 | START | 54 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `14` | `13` | 61 | START | 61 | 79 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 89 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 43–119
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_SnapReceive` | 43 | 50 | 8 | inferred_complete_timeline |
| `Action_None` | 51 | 53 | 3 | inferred_complete_timeline |
| `Action_Toss` | 54 | 60 | 7 | inferred_complete_timeline |
| `Action_None` | 61 | 119 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 69 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 89 | 18 | inferred_complete_timeline |
| `Action_None` | 90 | 122 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 53 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 89 | 25 | inferred_complete_timeline |
| `Action_None` | 90 | 108 | 19 | inferred_complete_timeline |
| `Action_None` | 110 | 113 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_BallSnap` | 37 | 44 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 58 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 61 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 47 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 89 | 26 | inferred_complete_timeline |
| `Action_None` | 90 | 114 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 126 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 49 | 13 | inferred_complete_timeline |
| `Action_None` | 53 | 73 | 21 | inferred_complete_timeline |
| `Action_None` | 76 | 88 | 13 | inferred_complete_timeline |
| `Action_None` | 90 | 100 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 66 | 30 | inferred_complete_timeline |
| `Action_None` | 68 | 117 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 50 | 14 | inferred_complete_timeline |
| `Action_None` | 58 | 61 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 159 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 108 | 72 | inferred_complete_timeline |
| `Action_None` | 116 | 117 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 7–66 | 60 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 28–116 | 53 | 4 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 40–72 | 33 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 49–113 | 64 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 53–112 | 59 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 56–122 | 64 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 64–200 | 111 | 2 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 73–74 | 2 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 109–115 | 7 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 117–119 | 3 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 120–132 | 13 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 121–230 | 108 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 122–151 | 23 | 3 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 127–168 | 40 | 2 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 128–239 | 94 | 3 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 128–133 | 6 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 142–152 | 11 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 201–202 | 2 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 203–239 | 37 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 209–234 | 6 | 2 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `14` (2 segments found)
- ⚠️ `Action_LeadBlock` for actor_track_id `15` (Position_Unknown): Annotated start 38 != Inferred start 40
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `7` (C): Annotated start 38 != Inferred start 52
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 438: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [37–50], lower_priority='Action_ZoneBlock' annotated_start=38, effective_Action_ZoneBlock_start=51.
- ⚠️ Action 'Action_None' range [37-126] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-108] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-66] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-117] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-53] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-89] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-108] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-159] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-47] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-114] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [37-44] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-58] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-61] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-69] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-122] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-49] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-73] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-88] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-100] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-50] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-61] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-66] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [28-44] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [61-79] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [115-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [40-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-119] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-95] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-113] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-60] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-72] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-200] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-115] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-225] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-131] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-146] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-149] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-168] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-217] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-133] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-152] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.

</details>