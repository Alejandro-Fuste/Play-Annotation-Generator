# Play-Annotation-Generator Annotation Review — RPO_116

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_116`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 31
- **Ball Tracks:** 1
- **Action Segments:** 109
- **Validation Warnings:** 116
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunPostRoute` | actor_track_id `16` | source `Route` | no temporal frame

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
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 47 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `1` | `1` | 54 | START | 54 | 139 |
| ✅ EXACT | `Action_ZoneBlock` | C | `10` | `10` | 54 | START | 54 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `6` | `6` | 54 | START | 54 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `7` | `7` | 54 | START | 54 | 99 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `8` | 54 | START | 54 | 58 |
| ✅ EXACT | `Action_ReadDefender` | QB | `4` | `4` | 57 | START | 57 | 81 |
| ✅ EXACT | `Action_PullBall` | QB | `4` | `4` | 82 | START | 82 | 91 |
| ✅ EXACT | `Action_ThrowPass` | QB | `4` | `4` | 130 | START | 130 | 139 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 56 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 57 | 81 | 25 | inferred_complete_timeline |
| `Action_PullBall` | 82 | 91 | 10 | inferred_complete_timeline |
| `Action_None` | 92 | 129 | 38 | inferred_complete_timeline |
| `Action_ThrowPass` | 130 | 139 | 10 | inferred_complete_timeline |
| `Action_None` | 140 | 163 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 52 | 4 | inferred_complete_timeline |
| `Action_None` | 53 | 168 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 92 | 40 | inferred_complete_timeline |
| `Action_None` | 95 | 132 | 38 | inferred_complete_timeline |
| `Action_None` | 136 | 161 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 53 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 99 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 139 | 37 | inferred_complete_timeline |
| `Action_None` | 140 | 169 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 53 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 139 | 86 | inferred_complete_timeline |
| `Action_None` | 140 | 174 | 35 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 53 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 139 | 86 | inferred_complete_timeline |
| `Action_None` | 140 | 145 | 6 | inferred_complete_timeline |
| `Action_None` | 152 | 157 | 6 | inferred_complete_timeline |
| `Action_None` | 159 | 165 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 53 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 133 | 80 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 139 | 4 | inferred_complete_timeline |
| `Action_None` | 140 | 154 | 15 | inferred_complete_timeline |
| `Action_None` | 156 | 159 | 4 | inferred_complete_timeline |
| `Action_None` | 161 | 171 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 53 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 58 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 58 | 6 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_None` | 73 | 117 | 45 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 142 | 3 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 148 | 162 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 53 | 136 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 90 | 38 | inferred_complete_timeline |
| `Action_None` | 92 | 98 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 158 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 127 | 75 | inferred_complete_timeline |
| `Action_None` | 132 | 162 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 7 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 19 | 4 | inferred_complete_timeline |
| `Action_None` | 53 | 168 | 116 | inferred_complete_timeline |
| `Action_None` | 171 | 389 | 219 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 29–64 | 12 | 4 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 43–70 | 25 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 66–389 | 315 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 72–131 | 40 | 4 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 73–170 | 43 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 96–114 | 13 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 115–117 | 3 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 130–165 | 27 | 4 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 133–176 | 44 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 137–183 | 47 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 144–389 | 242 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 147–360 | 212 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 147–187 | 29 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 194–389 | 196 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 278–282 | 5 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 304–361 | 31 | 5 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 328–335 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | 96 | 96 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 81 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_None' range [53-127] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-162] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-174] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-92] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-132] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-161] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-163] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-90] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-98] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-133] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '6' starts at frame 140, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [140-154] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-171] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-99] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-169] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '8' starts at frame 53, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [53-53] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-58] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-168] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-145] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-157] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-165] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-58] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-117] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-136] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-7] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-19] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-30] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-39] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-64] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-46] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-64] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-103] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-131] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-148] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-170] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-101] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-142] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-155] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-176] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-183] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-274] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-295] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-161] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-360] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-187] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-282] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-308] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-356] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-361] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-330] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '31' has 1 frames without a visible bounding box.
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