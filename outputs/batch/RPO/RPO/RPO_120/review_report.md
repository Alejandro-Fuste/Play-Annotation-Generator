# Play-Annotation-Generator Annotation Review — RPO_120

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_120`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 35
- **Ball Tracks:** 1
- **Action Segments:** 77
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunHitchRoute` | actor_track_id `39` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_ReadDefender` | DE1 | defense | `13` | `13` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 5 | START | 5 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 5 | START | 5 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 5 | START | 5 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 5 | START | 5 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 5 | START | 5 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 5 | START | 5 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 5 | START | 5 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 5 | START | 5 | 64 |
| ✅ EXACT | `Action_ZoneBlock` | C | `2` | `2` | 66 | START | 66 | 123 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `4` | 66 | START | 66 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `5` | `5` | 66 | START | 66 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `6` | `6` | 66 | START | 66 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `7` | 66 | START | 66 | 83 |
| ✅ EXACT | `Action_ReadDefender` | DE1 | `13` | `13` | 85 | START | 85 | 166 |
| ✅ EXACT | `Action_PullBall` | QB | `12` | `12` | 93 | START | 93 | 104 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 118 | START | 118 | 123 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 5–176
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_None` | 65 | 92 | 28 | inferred_complete_timeline |
| `Action_PullBall` | 93 | 104 | 12 | inferred_complete_timeline |
| `Action_None` | 105 | 117 | 13 | inferred_complete_timeline |
| `Action_ThrowPass` | 118 | 123 | 6 | inferred_complete_timeline |
| `Action_None` | 124 | 176 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 5–160
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_None` | 65 | 160 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 5–72
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_None` | 65 | 72 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 5–123
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_None` | 65 | 65 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 123 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 5–163
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_None` | 65 | 65 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 88 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 123 | 31 | inferred_complete_timeline |
| `Action_None` | 124 | 163 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 5–171
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_None` | 65 | 65 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 123 | 58 | inferred_complete_timeline |
| `Action_None` | 124 | 171 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 5–177
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_None` | 65 | 65 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 102 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 123 | 5 | inferred_complete_timeline |
| `Action_None` | 124 | 177 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 5–176
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_None` | 65 | 65 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 83 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 123 | 27 | inferred_complete_timeline |
| `Action_None` | 124 | 176 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 5–166
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_None` | 65 | 84 | 20 | inferred_complete_timeline |
| `Action_ReadDefender` | 85 | 166 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 5–119
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_None` | 65 | 119 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 5–168
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_None` | 65 | 147 | 83 | inferred_complete_timeline |
| `Action_None` | 153 | 168 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 5–99
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_None` | 65 | 92 | 28 | inferred_complete_timeline |
| `Action_None` | 95 | 99 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 5–133
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_None` | 65 | 133 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 5–177
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_None` | 65 | 177 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 5–115
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_None` | 65 | 115 | 51 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 71–173 | 85 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 87–93 | 7 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 87–179 | 59 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 96–299 | 204 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 119–194 | 72 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 122–149 | 28 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 137–144 | 8 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 143–144 | 2 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 147–153 | 6 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 150–266 | 117 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 152–170 | 19 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 158–299 | 141 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 161–299 | 139 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 170–299 | 129 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 173–299 | 127 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 209–299 | 91 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 225–228 | 4 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 253–299 | 47 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 254–299 | 46 | 1 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 275–280 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | 8 | 50 | 24 | 55.8% | 9–20, 31–34, 47–49 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 41 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [65-133] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-177] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-171] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-115] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-123] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-102] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-177] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-88] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-163] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-83] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-176] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-92] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-99] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-147] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-160] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-119] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-176] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [85-166] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-86] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-173] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-179] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-132] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-147] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-144] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-266] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-170] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-205] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-288] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-280] for track '35' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.

</details>