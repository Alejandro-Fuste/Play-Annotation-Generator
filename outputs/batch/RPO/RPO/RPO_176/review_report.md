# Play-Annotation-Generator Annotation Review — RPO_176

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_176`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunPostRoute` | actor_track_id `19` | source `Route` | no temporal frame

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
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 41 |
| ✅ EXACT | `Action_ZoneBlock` | C | `11` | `11` | 43 | START | 43 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `13` | 43 | START | 43 | 93 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `2` | 43 | START | 43 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `5` | `5` | 43 | START | 43 | 73 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `7` | 43 | START | 43 | 117 |
| ✅ EXACT | `Action_ReadDefender` | QB | `6` | `6` | 51 | START | 51 | 70 |
| ✅ EXACT | `Action_PullBall` | QB | `6` | `6` | 71 | START | 71 | 80 |
| ✅ EXACT | `Action_ThrowPass` | QB | `6` | `6` | 127 | START | 127 | 135 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 50 | 9 | inferred_complete_timeline |
| `Action_ReadDefender` | 51 | 70 | 20 | inferred_complete_timeline |
| `Action_PullBall` | 71 | 80 | 10 | inferred_complete_timeline |
| `Action_None` | 81 | 126 | 46 | inferred_complete_timeline |
| `Action_ThrowPass` | 127 | 135 | 9 | inferred_complete_timeline |
| `Action_None` | 136 | 150 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 149 | 108 | inferred_complete_timeline |
| `Action_None` | 153 | 160 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 99 | 58 | inferred_complete_timeline |
| `Action_None` | 102 | 126 | 25 | inferred_complete_timeline |
| `Action_None` | 129 | 152 | 24 | inferred_complete_timeline |
| `Action_None` | 163 | 177 | 15 | inferred_complete_timeline |
| `Action_None` | 179 | 202 | 24 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 42 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 135 | 93 | inferred_complete_timeline |
| `Action_None` | 136 | 155 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 42 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 73 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 135 | 15 | inferred_complete_timeline |
| `Action_None` | 136 | 167 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 42 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 135 | 93 | inferred_complete_timeline |
| `Action_None` | 139 | 153 | 15 | inferred_complete_timeline |
| `Action_None` | 157 | 164 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 25 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 29 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 36 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 93 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 107 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 129 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 135 | 4 | inferred_complete_timeline |
| `Action_None` | 136 | 160 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 42 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 117 | 75 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 51 | 10 | inferred_complete_timeline |
| `Action_None` | 79 | 163 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 65 | 24 | inferred_complete_timeline |
| `Action_None` | 132 | 159 | 28 | inferred_complete_timeline |
| `Action_None` | 162 | 173 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 162 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 85 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_None` | 42 | 122 | 81 | inferred_complete_timeline |
| `Action_None` | 155 | 185 | 31 | inferred_complete_timeline |
| `Action_None` | 187 | 210 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 210 | 169 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 57–86 | 30 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 66–153 | 88 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 76–158 | 64 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 98–132 | 35 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 108–210 | 93 | 5 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 109–159 | 46 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 119–210 | 92 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 136–137 | 2 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 162–165 | 4 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 187–210 | 24 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 195–210 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (LT) duration 93 frames exceeds threshold 90 frames [start=43, end=135].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (LG) duration 93 frames exceeds threshold 90 frames [start=43, end=135].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 93 frames exceeds threshold 90 frames [start=43, end=135].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (C) duration 93 frames exceeds threshold 90 frames [start=43, end=135].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (RG) duration 93 frames exceeds threshold 90 frames [start=43, end=135].
- ⚠️ Action 'Action_None' range [42-162] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-99] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-126] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-152] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-177] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-202] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-65] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-159] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-173] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [43-73] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-167] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [43-117] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-51] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-163] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-185] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-149] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-160] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [43-135] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-153] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-164] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-25] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-29] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [43-93] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-107] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-129] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-160] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-153] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-102] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-138] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-132] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-144] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-196] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-124] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-159] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '24' has 1 frames without a visible bounding box.
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