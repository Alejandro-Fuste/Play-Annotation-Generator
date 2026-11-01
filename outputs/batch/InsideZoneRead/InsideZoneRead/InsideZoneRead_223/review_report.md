# Play-Annotation-Generator Annotation Review — InsideZoneRead_223

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_223`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 6
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_ReadDefender` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | RG | offense | `7` | `6` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 75 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 76 | START | 76 | 92 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `13` | 79 | START | 93 | 117 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 79 | START | 79 | 169 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `4` | 79 | START | 79 | 169 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `7` | `6` | 79 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | RG | `7` | `6` | 92 | END | 76 | 92 |
| ✅ EXACT | `Action_ReadDefender` | RG | `7` | `6` | 96 | START | 96 | 108 |
| ✅ EXACT | `Action_Handoff` | RG | `7` | `6` | 109 | START | 109 | 115 |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `4` | `3` | 116 | START | 119 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `14` | `13` | 118 | START | 118 | 151 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 169 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 129 | 54 | inferred_complete_timeline |
| `Action_None` | 131 | 138 | 8 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 169 | 91 | inferred_complete_timeline |
| `Action_None` | 170 | 198 | 29 | inferred_complete_timeline |
| `Action_None` | 204 | 299 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_BallSnap` | 76 | 92 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 117 | 25 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 118 | 151 | 34 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 157 | 169 | 13 | inferred_complete_timeline |
| `Action_None` | 170 | 192 | 23 | inferred_complete_timeline |
| `Action_None` | 196 | 299 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_SnapReceive` | 76 | 92 | 17 | inferred_complete_timeline |
| `Action_None` | 93 | 95 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 96 | 108 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 109 | 115 | 7 | inferred_complete_timeline |
| `Action_None` | 116 | 170 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 169 | 91 | inferred_complete_timeline |
| `Action_None` | 170 | 205 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 299 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 63 | 4 | inferred_complete_timeline |
| `Action_None` | 84 | 190 | 107 | inferred_complete_timeline |
| `Action_None` | 192 | 206 | 15 | inferred_complete_timeline |
| `Action_None` | 210 | 299 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 69 | 7 | inferred_complete_timeline |
| `Action_None` | 79 | 81 | 3 | inferred_complete_timeline |
| `Action_None` | 83 | 88 | 6 | inferred_complete_timeline |
| `Action_None` | 101 | 113 | 13 | inferred_complete_timeline |
| `Action_None` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_None` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_None` | 124 | 299 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–273
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 138 | 63 | inferred_complete_timeline |
| `Action_None` | 145 | 273 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 129 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 143 | 68 | inferred_complete_timeline |
| `Action_None` | 145 | 149 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 104 | 29 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_None` | 109 | 118 | 10 | inferred_complete_timeline |
| `Action_None` | 128 | 222 | 95 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–179 | 180 | 2 | Undefined position; Undefined team |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–203 | 199 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 84–259 | 176 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 137–139 | 3 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 141–145 | 5 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 148–299 | 147 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 150–151 | 2 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 155–299 | 144 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 160–161 | 2 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 165–299 | 135 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 168–284 | 117 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 169–299 | 131 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 170–299 | 124 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 175–235 | 59 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 181–299 | 114 | 4 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 192–214 | 16 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 202–299 | 91 | 3 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 228–240 | 13 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 255–256 | 2 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 257–296 | 12 | 5 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 79 != Inferred start 93
- ❌ Missing segment for action `Action_ZoneBlock` on target `7` (RG)
- ⚠️ `Action_BallCarry` for actor_track_id `4` (Position_Unknown): Annotated start 116 != Inferred start 119
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 445: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 446: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (LT) duration 91 frames exceeds threshold 90 frames [start=79, end=169].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (RT) duration 91 frames exceeds threshold 90 frames [start=79, end=169].
- ⚠️ Segment 'Action_ZoneBlock' for track '6' has invalid range: start=79, end=75. Clamping end to start.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [76–92], lower_priority='Action_ZoneBlock' annotated_start=79, effective_Action_ZoneBlock_start=93.
- ⚠️ Action 'Action_None' range [76-129] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-138] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-198] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-179] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [119-203] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-205] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-170] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-138] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-273] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-63] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-206] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-104] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-118] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-222] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-69] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-81] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-129] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [118-151] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 170, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [170-192] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-259] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-177] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-172] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-284] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-212] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-208] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-220] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-235] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-259] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-275] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-214] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-233] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-240] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>