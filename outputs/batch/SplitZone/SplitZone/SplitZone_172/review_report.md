# Play-Annotation-Generator Annotation Review — SplitZone_172

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_172`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 1
- **Action Segments:** 80
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LB2 | defense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | TE2 | offense | `17` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `13` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 11 | START | 12 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `14` | `Group` | 11 | START | 12 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 11 | START | 12 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 11 | START | 12 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 11 | START | 12 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 11 | START | 12 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 11 | START | 12 | 75 |
| ✅ EXACT | `Action_BallSnap` | LB2 | `11` | `11` | 73 | START | 73 | 85 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `4` | `4` | 76 | START | 76 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `5` | `5` | 76 | START | 76 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `6` | `6` | 76 | START | 76 | 90 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `9` | `9` | 76 | START | 76 | 147 |
| ✅ EXACT | `Action_SplitBlock` | TE2 | `17` | `17` | 79 | START | 79 | 147 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 85 | END | 73 | 85 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `10` | 91 | START | 91 | 98 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `13` | `13` | 99 | START | 99 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 147 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 12–163
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 72 | 61 | inferred_complete_timeline |
| `Action_SnapReceive` | 73 | 85 | 13 | inferred_complete_timeline |
| `Action_None` | 86 | 90 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 91 | 98 | 8 | inferred_complete_timeline |
| `Action_None` | 99 | 108 | 10 | inferred_complete_timeline |
| `Action_None` | 111 | 163 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 12–137
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 72 | 61 | inferred_complete_timeline |
| `Action_None` | 73 | 137 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 12–147
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 78 | 67 | inferred_complete_timeline |
| `Action_SplitBlock` | 79 | 147 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 12–91
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 75 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 86 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 91 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 12–160
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 75 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 147 | 72 | inferred_complete_timeline |
| `Action_None` | 148 | 160 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 12–129
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 75 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 129 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 12–112
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 75 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 90 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 103 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 112 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 12–146
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 72 | 61 | inferred_complete_timeline |
| `Action_None` | 73 | 146 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 12–172
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 72 | 61 | inferred_complete_timeline |
| `Action_None` | 73 | 110 | 38 | inferred_complete_timeline |
| `Action_None` | 112 | 118 | 7 | inferred_complete_timeline |
| `Action_None` | 120 | 124 | 5 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 130 | 164 | 35 | inferred_complete_timeline |
| `Action_None` | 168 | 172 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 12–154
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 72 | 61 | inferred_complete_timeline |
| `Action_None` | 73 | 117 | 45 | inferred_complete_timeline |
| `Action_None` | 121 | 146 | 26 | inferred_complete_timeline |
| `Action_None` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 154 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 12–193
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 72 | 61 | inferred_complete_timeline |
| `Action_None` | 73 | 189 | 117 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 12–133
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 72 | 61 | inferred_complete_timeline |
| `Action_None` | 73 | 133 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 12–152
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 72 | 61 | inferred_complete_timeline |
| `Action_None` | 73 | 152 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 12–139
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 72 | 61 | inferred_complete_timeline |
| `Action_BallSnap` | 73 | 85 | 13 | inferred_complete_timeline |
| `Action_None` | 86 | 135 | 50 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 12–233
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 72 | 61 | inferred_complete_timeline |
| `Action_None` | 73 | 233 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 12–148
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 72 | 61 | inferred_complete_timeline |
| `Action_None` | 73 | 148 | 76 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 12–211 | 198 | 4 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 12–239 | 225 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 109–168 | 58 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 139–205 | 67 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 143–155 | 13 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 151–169 | 4 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 168–239 | 72 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 168–239 | 72 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 171–232 | 60 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 174–213 | 36 | 4 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 177–186 | 10 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 178–190 | 8 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 190–239 | 50 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 197–235 | 39 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 200–207 | 8 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 204–206 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | 48 | 51 | 3 | 75.0% | 49 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 346: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 346: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [73-152] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-181] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-211] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-110] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-118] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-124] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-164] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-233] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-129] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-86] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-91] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-90] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-103] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-112] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-189] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-133] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-160] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-108] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-163] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-135] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-146] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-146] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-148] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [79-147] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-155] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-184] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-220] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-232] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-190] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-205] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-186] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-182] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-235] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-207] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>