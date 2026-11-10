# Play-Annotation-Generator Annotation Review — RPO_60

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_60`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSeamRoute` | actor_track_id `2` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 47 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `0` | `0` | 49 | START | 49 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `1` | `1` | 49 | START | 49 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `12` | 49 | START | 76 | 77 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `5` | 49 | START | 49 | 112 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `9` | 49 | START | 49 | 70 |
| ✅ EXACT | `Action_ReadDefender` | QB | `7` | `7` | 50 | START | 50 | 70 |
| ✅ EXACT | `Action_PullBall` | QB | `7` | `7` | 71 | START | 71 | 89 |
| ✅ EXACT | `Action_ThrowPass` | QB | `7` | `7` | 102 | START | 102 | 112 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 50 | 70 | 21 | inferred_complete_timeline |
| `Action_PullBall` | 71 | 89 | 19 | inferred_complete_timeline |
| `Action_None` | 90 | 101 | 12 | inferred_complete_timeline |
| `Action_ThrowPass` | 102 | 112 | 11 | inferred_complete_timeline |
| `Action_None` | 113 | 210 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 123 | 76 | inferred_complete_timeline |
| `Action_None` | 132 | 210 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 190 | 143 | inferred_complete_timeline |
| `Action_None` | 192 | 210 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 48 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 112 | 64 | inferred_complete_timeline |
| `Action_None` | 113 | 210 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 48 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 112 | 64 | inferred_complete_timeline |
| `Action_None` | 113 | 127 | 15 | inferred_complete_timeline |
| `Action_None` | 153 | 210 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 48 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 112 | 34 | inferred_complete_timeline |
| `Action_None` | 113 | 139 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 48 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 70 | 22 | inferred_complete_timeline |
| `Action_None` | 129 | 158 | 30 | inferred_complete_timeline |
| `Action_None` | 174 | 210 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 48 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 69 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 112 | 38 | inferred_complete_timeline |
| `Action_None` | 113 | 142 | 30 | inferred_complete_timeline |
| `Action_None` | 144 | 148 | 5 | inferred_complete_timeline |
| `Action_None` | 153 | 210 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 134 | 87 | inferred_complete_timeline |
| `Action_None` | 143 | 210 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–51
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 51 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 66 | 19 | inferred_complete_timeline |
| `Action_None` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 96 | 12 | inferred_complete_timeline |
| `Action_None` | 98 | 104 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 149 | 102 | inferred_complete_timeline |
| `Action_None` | 153 | 210 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 122 | 75 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 48–81 | 33 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 58–210 | 143 | 4 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 93–101 | 9 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 96–104 | 9 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 103–104 | 2 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 115–210 | 96 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 119–151 | 30 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 133–210 | 27 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 142–210 | 63 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 144–210 | 67 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 154–188 | 35 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 165–210 | 46 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 53 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [113-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-69] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-142] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-148] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-190] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-149] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-127] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-123] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-134] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-70] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-158] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-51] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-66] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-96] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '12' starts at frame 48, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [48-48] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-112] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-56] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-81] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-96] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-101] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-149] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-160] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-207] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '24' has 1 frames without a visible bounding box.
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