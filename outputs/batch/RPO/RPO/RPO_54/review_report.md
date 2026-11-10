# Play-Annotation-Generator Annotation Review — RPO_54

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_54`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 74
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `18` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBall` | RB | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | RB | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `17` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `11` | 48 | START | 48 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `12` | `12` | 48 | START | 48 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 48 | START | 48 | 64 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `4` | 48 | START | 48 | 106 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `8` | 48 | START | 48 | 69 |
| ✅ EXACT | `Action_ReadDefender` | QB | `6` | `6` | 51 | START | 51 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBall` | RB | `5` | `5` | 71 | START | 71 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | RB | `5` | `5` | 99 | START | 99 | 102 |

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
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 50 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 51 | 75 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 70 | 24 | inferred_complete_timeline |
| `Action_PullBall` | 71 | 76 | 6 | inferred_complete_timeline |
| `Action_PullBall` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_None` | 83 | 98 | 16 | inferred_complete_timeline |
| `Action_ThrowPass` | 99 | 102 | 4 | inferred_complete_timeline |
| `Action_ThrowPass` | 104 | 106 | 3 | inferred_complete_timeline |
| `Action_None` | 107 | 180 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 100–172
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 100 | 114 | 15 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_None` | 123 | 135 | 13 | inferred_complete_timeline |
| `Action_None` | 139 | 169 | 31 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 47 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 106 | 59 | inferred_complete_timeline |
| `Action_None` | 107 | 148 | 42 | inferred_complete_timeline |
| `Action_None` | 150 | 180 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 47 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 58 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 106 | 44 | inferred_complete_timeline |
| `Action_None` | 107 | 161 | 55 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 170 | 4 | inferred_complete_timeline |
| `Action_None` | 175 | 179 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 47 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 64 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 100 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 47 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 66 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 106 | 36 | inferred_complete_timeline |
| `Action_None` | 107 | 180 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 47 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 69 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 114 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 94 | 48 | inferred_complete_timeline |
| `Action_None` | 143 | 180 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 79 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 124 | 78 | inferred_complete_timeline |
| `Action_None` | 127 | 180 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 93 | 47 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_None` | 109 | 116 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 180 | 134 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–177 | 154 | 5 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 42–154 | 103 | 5 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 95–180 | 86 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 100–104 | 5 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 101–175 | 75 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 116–155 | 40 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 116–180 | 65 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 134–180 | 47 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 136–163 | 26 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 147–180 | 34 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 160–180 | 21 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBall` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ThrowPass` and target `5` (2 segments found)

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
| Missing visible bounding boxes during action | 51 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [47-124] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-93] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-116] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-114] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-180] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-148] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-70] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBall' range [71-76] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [99-102] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [51-75] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-61] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-124] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-163] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-69] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-94] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-180] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-79] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-66] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-69] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-58] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-161] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-64] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-118] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-144] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-154] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-114] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-169] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-175] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-155] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-180] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-163] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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