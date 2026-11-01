# Play-Annotation-Generator Annotation Review — InsideZoneRead_260

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_260`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 117
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 5
- **Group Expanded Events:** 4
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `16` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Keep` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 13 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `16` | `14` | 14 | START | 29 | 31 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `1` | 17 | START | 17 | 72 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `4` | `3` | 17 | START | 17 | 89 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 31 | END | 14 | 31 |
| ✅ EXACT | `Action_ReadDefender` | QB | `5` | `4` | 34 | START | 34 | 38 |
| ✅ EXACT | `Action_Keep` | QB | `5` | `4` | 39 | START | 39 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `5` | `4` | 65 | START | 65 | 190 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 89 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_SnapReceive` | 14 | 31 | 18 | inferred_complete_timeline |
| `Action_None` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 34 | 38 | 5 | inferred_complete_timeline |
| `Action_Keep` | 39 | 64 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 65 | 190 | 126 | inferred_complete_timeline |
| `Action_BallCarry` | 202 | 210 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 48 | 35 | inferred_complete_timeline |
| `Action_None` | 60 | 78 | 19 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 89 | 73 | inferred_complete_timeline |
| `Action_None` | 90 | 151 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 72 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 76 | 63 | inferred_complete_timeline |
| `Action_None` | 78 | 210 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 54 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 65 | 52 | inferred_complete_timeline |
| `Action_None` | 84 | 104 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 19 | 6 | inferred_complete_timeline |
| `Action_None` | 108 | 123 | 16 | inferred_complete_timeline |
| `Action_None` | 163 | 165 | 3 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 176 | 210 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–4
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 54 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–210 | 184 | 8 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–210 | 186 | 5 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–128 | 126 | 3 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 22–95 | 42 | 3 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 29–210 | 169 | 5 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 54–118 | 8 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 64–210 | 125 | 5 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 65–210 | 146 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 65–210 | 128 | 6 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 83–115 | 29 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 84–210 | 127 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 93–173 | 73 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 99–167 | 56 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 132–210 | 76 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 157–210 | 54 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 159–210 | 51 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 164–178 | 15 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 197–210 | 14 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 199–210 | 12 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 205–206 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `16` (Position_Unknown): Annotated start 14 != Inferred start 29
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 73 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 520: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 520: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [14-45] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-60] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-110] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-159] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-72] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-54] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-151] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [65-190] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [202-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-48] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-78] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-54] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-37] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-46] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-99] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-37] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-76] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-210] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-19] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-123] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-65] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-104] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-46] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-92] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-75] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-179] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-80] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-170] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-190] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-210] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-88] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-105] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-139] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-170] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-109] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-210] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-96] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-163] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-167] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-176] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-210] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-164] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-178] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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

</details>