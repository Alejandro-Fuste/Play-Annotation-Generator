# Play-Annotation-Generator Annotation Review — DeepCross_69

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_69`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Comp.`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_RunDeepCrossRoute` | CB3 | defense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | CB3 | defense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 16 | START | 16 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `14` | 19 | START | 31 | 55 |
| ✅ EXACT | `Action_PassBlock` | RG | `15` | `15` | 19 | START | 19 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `19` | `19` | 19 | START | 19 | 51 |
| ✅ EXACT | `Action_PassBlock` | LG | `20` | `20` | 19 | START | 19 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `21` | 19 | START | 19 | 123 |
| ✅ EXACT | `Action_RunDeepCrossRoute` | CB3 | `5` | `5` | 30 | START | 30 | 186 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 30 | END | 16 | 30 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 107 | START | 107 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | CB3 | `5` | `5` | 195 | START | 195 | 196 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 30 | 15 | inferred_complete_timeline |
| `Action_None` | 31 | 106 | 76 | inferred_complete_timeline |
| `Action_ThrowPass` | 107 | 119 | 13 | inferred_complete_timeline |
| `Action_None` | 120 | 152 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 107 | 92 | inferred_complete_timeline |
| `Action_None` | 111 | 156 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 175 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 239 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 51 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 168 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 174 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_BallSnap` | 16 | 30 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 55 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 125 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 38 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 123 | 105 | inferred_complete_timeline |
| `Action_PassBlock` | 126 | 156 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 158 | 159 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 133 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 114 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 129 | 114 | inferred_complete_timeline |
| `Action_None` | 132 | 156 | 25 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 190 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 156 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 111 | 96 | inferred_complete_timeline |
| `Action_None` | 114 | 118 | 5 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_None` | 134 | 150 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 239 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 30 | 186 | 157 | inferred_complete_timeline |
| `Action_None` | 187 | 194 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 205 | 213 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 222 | 224 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 226 | 228 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 156 | 141 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 162 | 169 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 239 | 224 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 31–33 | 3 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 35–153 | 111 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 87–88 | 2 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 113–182 | 70 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 123–125 | 3 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 144–195 | 46 | 4 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 164–165 | 2 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 166–169 | 4 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 198–239 | 41 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 203–216 | 13 | 2 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 226–234 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 72: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 72: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 72: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [16–30], lower_priority='Action_PassBlock' annotated_start=19, effective_Action_PassBlock_start=31.
- ⚠️ Action 'Action_None' range [16-133] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-107] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-156] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-111] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-118] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-150] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-156] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-156] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [30-186] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [195-196] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [205-213] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [222-224] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [226-228] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-190] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-129] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-156] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-114] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-175] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-152] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-55] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [57-125] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-51] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-174] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-123] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [126-156] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [158-159] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-33] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-37] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-57] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-122] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-153] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-182] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-154] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-172] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-186] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-216] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-234] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>