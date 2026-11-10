# Play-Annotation-Generator Annotation Review — RPO_252

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_252`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 1
- **Action Segments:** 60
- **Validation Warnings:** 52
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunFadeRoute` | actor_track_id `28` | source `Route` | no temporal frame

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
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_ReadDefender` | DE2 | defense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `7` | `7` |
| ✅ EXACT | `Action_PullBall` | DE2 | defense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | DE2 | defense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 17 | START | 12 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 17 | START | 12 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 17 | START | 12 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 17 | START | 12 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 17 | START | 12 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 17 | START | 12 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 17 | START | 12 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 17 | START | 12 | 50 |
| ✅ EXACT | `Action_ReadDefender` | DE2 | `12` | `12` | 43 | START | 43 | 68 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `13` | `13` | 52 | START | 52 | 106 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 52 | START | 52 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `3` | `3` | 52 | START | 52 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `6` | `6` | 52 | START | 52 | 99 |
| ✅ EXACT | `Action_ZoneBlock` | C | `7` | `7` | 52 | START | 52 | 114 |
| ✅ EXACT | `Action_PullBall` | DE2 | `12` | `12` | 69 | START | 69 | 80 |
| ✅ EXACT | `Action_ThrowPass` | DE2 | `12` | `12` | 108 | START | 108 | 114 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 12–129
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 50 | 39 | inferred_complete_timeline |
| `Action_None` | 51 | 125 | 75 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 12–117
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 50 | 39 | inferred_complete_timeline |
| `Action_None` | 51 | 117 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 12–111
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 50 | 39 | inferred_complete_timeline |
| `Action_None` | 51 | 111 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 12–116
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 50 | 39 | inferred_complete_timeline |
| `Action_None` | 51 | 51 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 78 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 109 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 114 | 4 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 12–125
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 50 | 39 | inferred_complete_timeline |
| `Action_None` | 51 | 51 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 99 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 114 | 13 | inferred_complete_timeline |
| `Action_None` | 115 | 125 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 12–121
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 50 | 39 | inferred_complete_timeline |
| `Action_None` | 51 | 51 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 114 | 63 | inferred_complete_timeline |
| `Action_None` | 115 | 121 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 12–106
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 50 | 39 | inferred_complete_timeline |
| `Action_None` | 51 | 51 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 106 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 12–114
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 50 | 39 | inferred_complete_timeline |
| `Action_None` | 51 | 51 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 114 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 12–133
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 50 | 39 | inferred_complete_timeline |
| `Action_None` | 51 | 133 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 12–116
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 42 | 31 | inferred_complete_timeline |
| `Action_ReadDefender` | 43 | 68 | 26 | inferred_complete_timeline |
| `Action_PullBall` | 69 | 80 | 12 | inferred_complete_timeline |
| `Action_None` | 81 | 107 | 27 | inferred_complete_timeline |
| `Action_ThrowPass` | 108 | 114 | 7 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 12–127
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 50 | 39 | inferred_complete_timeline |
| `Action_None` | 51 | 127 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 12–125
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 50 | 39 | inferred_complete_timeline |
| `Action_None` | 51 | 125 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 12–127
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 50 | 39 | inferred_complete_timeline |
| `Action_None` | 51 | 127 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 12–112
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 50 | 39 | inferred_complete_timeline |
| `Action_None` | 51 | 112 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 12–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 50 | 39 | inferred_complete_timeline |
| `Action_None` | 51 | 171 | 121 | inferred_complete_timeline |
| `Action_None` | 173 | 180 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 37–114 | 78 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 65–67 | 3 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 71–105 | 35 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 73–103 | 4 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 79–116 | 24 | 3 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 88–89 | 2 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 100–119 | 20 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 128–180 | 53 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 133–180 | 48 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | 12 | 43 | 32 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 33 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [51-127] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-112] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-114] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-78] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-109] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [111-114] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-133] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-171] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-99] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-125] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-121] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-125] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-127] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-106] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-111] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-114] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-67] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-105] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-85] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-116] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-119] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-180] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-180] for track '24' has 2 frames without a visible bounding box.
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