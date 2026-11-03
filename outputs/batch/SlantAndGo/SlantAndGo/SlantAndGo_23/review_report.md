# Play-Annotation-Generator Annotation Review — SlantAndGo_23

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_23`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 73
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB3 | defense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `6` | `6` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | SAF1 | defense | `12` | `12` |
| ✅ EXACT | `Action_SellRoute` | WR3 | offense | `4` | `4` |
| ✅ EXACT | `Action_ThrowPass` | SAF1 | defense | `12` | `12` |
| ✅ EXACT | `Action_VerticalStem` | WR3 | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 8 |
| ✅ EXACT | `Action_BallSnap` | CB3 | `17` | `17` | 6 | START | 6 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `18` | `18` | 9 | START | 9 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 9 | START | 9 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `6` | `6` | 9 | START | 9 | 130 |
| ✅ EXACT | `Action_PassBlock` | RG | `9` | `9` | 9 | START | 9 | 161 |
| ✅ EXACT | `Action_SnapReceive` | SAF1 | `12` | `12` | 24 | END | 6 | 24 |
| ✅ EXACT | `Action_SellRoute` | WR3 | `4` | `4` | 62 | START | 62 | 98 |
| ✅ EXACT | `Action_ThrowPass` | SAF1 | `12` | `12` | 87 | START | 87 | 94 |
| ✅ EXACT | `Action_VerticalStem` | WR3 | `4` | `4` | 99 | START | 99 | 187 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 69 | 64 | inferred_complete_timeline |
| `Action_None` | 96 | 125 | 30 | inferred_complete_timeline |
| `Action_None` | 127 | 136 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 155 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_SellRoute` | 62 | 98 | 37 | inferred_complete_timeline |
| `Action_VerticalStem` | 99 | 187 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 145 | 137 | inferred_complete_timeline |
| `Action_PassBlock` | 147 | 153 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 63 | 55 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 87 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 161 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 130 | 122 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 140 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 167 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 36 | 31 | inferred_complete_timeline |
| `Action_None` | 41 | 105 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 105 | 100 | inferred_complete_timeline |
| `Action_None` | 109 | 145 | 37 | inferred_complete_timeline |
| `Action_None` | 161 | 165 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 47 | 42 | inferred_complete_timeline |
| `Action_None` | 51 | 93 | 43 | inferred_complete_timeline |
| `Action_None` | 97 | 103 | 7 | inferred_complete_timeline |
| `Action_None` | 107 | 150 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 182 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 175 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–181
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 181 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 190 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_BallSnap` | 6 | 24 | 19 | inferred_complete_timeline |
| `Action_None` | 25 | 176 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_SnapReceive` | 6 | 24 | 19 | inferred_complete_timeline |
| `Action_None` | 25 | 86 | 62 | inferred_complete_timeline |
| `Action_ThrowPass` | 87 | 94 | 8 | inferred_complete_timeline |
| `Action_None` | 95 | 109 | 15 | inferred_complete_timeline |
| `Action_None` | 111 | 138 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 177 | 172 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–161 | 154 | 5 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–189 | 182 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 97–98 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 108–109 | 2 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 115–116 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 123–134 | 12 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 215–239 | 24 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 218–239 | 22 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 224–239 | 16 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 237–238 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 36: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ Row 36: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ Row 36: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Row 36: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [6-155] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-111] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-126] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-161] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-181] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-190] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [99-187] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-130] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-140] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-177] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-36] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-105] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-109] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-138] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-69] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-125] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-136] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-115] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-189] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-47] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-93] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-103] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-150] for track '15' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-167] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-176] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-145] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [147-153] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-182] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-105] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-145] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-63] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-87] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-134] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-239] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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