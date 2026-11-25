# Play-Annotation-Generator Annotation Review — InsideZoneRead_266

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_266`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 99
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
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `18` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | DE2 | defense | `13` | `12` |
| ✅ EXACT | `Action_ReadDefender` | DE2 | defense | `13` | `12` |
| ✅ EXACT | `Action_Keep` | DE2 | defense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE2 | defense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 18 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `18` | `16` | 16 | START | 93 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `1` | `0` | 19 | START | 19 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 19 | START | 19 | 91 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 19 | START | 19 | 94 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `5` | 19 | START | 19 | 95 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `7` | 19 | START | 19 | 96 |
| ✅ EXACT | `Action_SnapReceive` | DE2 | `13` | `12` | 30 | END | 16 | 30 |
| ✅ EXACT | `Action_ReadDefender` | DE2 | `13` | `12` | 35 | START | 35 | 41 |
| ✅ EXACT | `Action_Keep` | DE2 | `13` | `12` | 42 | START | 42 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE2 | `13` | `12` | 57 | START | 57 | 75 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 96 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 156 | 141 | inferred_complete_timeline |
| `Action_None` | 158 | 172 | 15 | inferred_complete_timeline |
| `Action_None` | 174 | 210 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 64 | 49 | inferred_complete_timeline |
| `Action_None` | 67 | 172 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 94 | 76 | inferred_complete_timeline |
| `Action_None` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_None` | 102 | 110 | 9 | inferred_complete_timeline |
| `Action_None` | 124 | 171 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 95 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 91 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_None` | 97 | 175 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 96 | 78 | inferred_complete_timeline |
| `Action_None` | 97 | 102 | 6 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_None` | 108 | 110 | 3 | inferred_complete_timeline |
| `Action_None` | 114 | 153 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 96 | 78 | inferred_complete_timeline |
| `Action_None` | 97 | 125 | 29 | inferred_complete_timeline |
| `Action_None` | 130 | 210 | 81 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 52 | 37 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_None` | 83 | 87 | 5 | inferred_complete_timeline |
| `Action_None` | 91 | 152 | 62 | inferred_complete_timeline |
| `Action_None` | 156 | 172 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 30 | 15 | inferred_complete_timeline |
| `Action_None` | 31 | 34 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 35 | 41 | 7 | inferred_complete_timeline |
| `Action_Keep` | 42 | 56 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 57 | 75 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 77 | 116 | 40 | inferred_complete_timeline |
| `Action_BallCarry` | 123 | 173 | 51 | inferred_complete_timeline |
| `Action_BallCarry` | 175 | 179 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 55 | 40 | inferred_complete_timeline |
| `Action_None` | 95 | 116 | 22 | inferred_complete_timeline |
| `Action_None` | 138 | 148 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 116 | 101 | inferred_complete_timeline |
| `Action_None` | 177 | 193 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 110 | 95 | inferred_complete_timeline |
| `Action_None` | 119 | 142 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 63 | 48 | inferred_complete_timeline |
| `Action_None` | 68 | 88 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–25
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 25 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 210 | 195 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `17` | Position_Unknown | Team_Unknown | 68–210 | 127 | 3 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 93–174 | 82 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 97–118 | 22 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 120–161 | 42 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 122–141 | 16 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 123–178 | 56 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 125–180 | 56 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 130–185 | 56 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 145–146 | 2 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 163–164 | 2 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 167–168 | 2 | 1 | Undefined position; Undefined team |
| `26` | `42` | Position_Unknown | Team_Unknown | 176–192 | 17 | 1 | Undefined position; Undefined team |
| `27` | `43` | Position_Unknown | Team_Unknown | 176–177 | 2 | 1 | Undefined position; Undefined team |
| `28` | `45` | Position_Unknown | Team_Unknown | 179–182 | 4 | 1 | Undefined position; Undefined team |
| `29` | `46` | Position_Unknown | Team_Unknown | 181–210 | 30 | 1 | Undefined position; Undefined team |
| `30` | `49` | Position_Unknown | Team_Unknown | 185–191 | 7 | 1 | Undefined position; Undefined team |
| `31` | `51` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |
| `32` | `52` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `18` (Position_Unknown): Annotated start 16 != Inferred start 93
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '16' has invalid range: start=93, end=30. Clamping end to start.
- ⚠️ Action 'Action_None' range [97-125] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-210] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-94] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-110] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-171] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-25] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-63] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-88] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-64] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-172] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-95] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-110] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-102] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-153] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-116] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-193] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-210] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-52] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-87] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-152] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-172] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-156] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-172] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [57-75] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [77-116] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [123-173] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [175-179] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-175] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-55] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-116] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-148] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-75] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-210] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-118] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-161] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-131] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-178] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-185] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-192] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-191] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '32' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_266'; source metadata written as null.

</details>