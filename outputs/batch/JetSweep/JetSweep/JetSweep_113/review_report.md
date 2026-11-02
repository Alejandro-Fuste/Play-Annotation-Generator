# Play-Annotation-Generator Annotation Review — JetSweep_113

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_113`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_LeadBlock` | TE2 | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | DT1 | defense | `14` | `13` |
| ✅ EXACT | `Action_Toss` | DT1 | defense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `12` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 17 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 55 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `17` | `16` | 51 | START | 51 | 89 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 54 | START | 54 | 71 |
| ✅ EXACT | `Action_LeadBlock` | TE2 | `12` | `11` | 56 | START | 56 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `11` | `10` | 56 | START | 56 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `14` | 56 | START | 72 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `6` | `5` | 56 | START | 56 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `8` | `7` | 56 | START | 56 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `8` | 56 | START | 56 | 71 |
| ✅ EXACT | `Action_SnapReceive` | DT1 | `14` | `13` | 71 | END | 54 | 71 |
| ✅ EXACT | `Action_Toss` | DT1 | `14` | `13` | 78 | START | 78 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `17` | `16` | 90 | START | 90 | 100 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 162 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 127 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_LeadBlock` | 56 | 162 | 107 | inferred_complete_timeline |
| `Action_None` | 163 | 183 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 162 | 107 | inferred_complete_timeline |
| `Action_None` | 163 | 199 | 37 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 85 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 105 | 162 | 58 | inferred_complete_timeline |
| `Action_None` | 163 | 166 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 17–136
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 53 | 37 | inferred_complete_timeline |
| `Action_BallSnap` | 54 | 71 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 95 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 110 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 121 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 126 | 131 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 136 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 71 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 114 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 132 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 162 | 28 | inferred_complete_timeline |
| `Action_None` | 163 | 210 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 115 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 118 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 130 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 210 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 7–210
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 53 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 54 | 71 | 18 | inferred_complete_timeline |
| `Action_None` | 72 | 77 | 6 | inferred_complete_timeline |
| `Action_Toss` | 78 | 89 | 12 | inferred_complete_timeline |
| `Action_None` | 90 | 163 | 74 | inferred_complete_timeline |
| `Action_None` | 198 | 210 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 210 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 100 | 47 | inferred_complete_timeline |
| `Action_None` | 102 | 158 | 57 | inferred_complete_timeline |
| `Action_None` | 162 | 164 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 2–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 53 | 52 | inferred_complete_timeline |
| `Action_None` | 54 | 210 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 210 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 210 | 157 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 30–82 | 18 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 50–184 | 127 | 6 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 80–210 | 106 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 83–114 | 32 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 95–97 | 3 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 100–146 | 47 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 126–210 | 80 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 129–130 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 131–154 | 21 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 135–195 | 33 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 146–210 | 63 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 151–210 | 57 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 161–210 | 50 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 177–210 | 34 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 194–210 | 17 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 194–210 | 17 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 200–210 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 228: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (LG) duration 107 frames exceeds threshold 90 frames [start=56, end=162].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (LT) duration 107 frames exceeds threshold 90 frames [start=56, end=162].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (RG) duration 107 frames exceeds threshold 90 frames [start=56, end=162].
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '11' (TE2) duration 107 frames exceeds threshold 90 frames [start=56, end=162].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [54–71], lower_priority='Action_ZoneBlock' annotated_start=56, effective_Action_ZoneBlock_start=72.
- ⚠️ Action 'Action_None' range [54-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-130] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-127] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-85] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-100] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-158] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-199] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-71] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [75-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [116-132] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-115] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-118] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-183] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-163] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-110] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [126-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-136] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-73] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-82] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [51-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [90-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [103-132] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [138-181] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [183-184] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-179] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-114] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-146] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-201] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-144] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-154] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-164] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-166] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-184] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '31' has 1 frames without a visible bounding box.
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

</details>