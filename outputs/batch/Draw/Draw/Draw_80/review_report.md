# Play-Annotation-Generator Annotation Review — Draw_80

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `Draw_80`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 96
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 3
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `1` | `0` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `2` | `1` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `1` | `0` | 15 | START | 15 | 88 |
| ✅ EXACT | `Action_PassBlock` | RG | `2` | `1` | 15 | START | 15 | 63 |
| ✅ EXACT | `Action_PassBlock` | RT | `7` | `6` | 15 | START | 15 | 89 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 28 | END | 28 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `8` | `7` | 47 | START | 47 | 72 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 89 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_SnapReceive` | 28 | 28 | 1 | inferred_complete_timeline |
| `Action_None` | 29 | 46 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 47 | 72 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 74 | 131 | 58 | inferred_complete_timeline |
| `Action_BallCarry` | 172 | 239 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 88 | 74 | inferred_complete_timeline |
| `Action_None` | 90 | 154 | 65 | inferred_complete_timeline |
| `Action_None` | 159 | 212 | 54 | inferred_complete_timeline |
| `Action_None` | 215 | 239 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 63 | 49 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_None` | 102 | 115 | 14 | inferred_complete_timeline |
| `Action_None` | 117 | 120 | 4 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_None` | 145 | 152 | 8 | inferred_complete_timeline |
| `Action_None` | 154 | 239 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 89 | 75 | inferred_complete_timeline |
| `Action_None` | 90 | 226 | 137 | inferred_complete_timeline |
| `Action_None` | 230 | 239 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 234 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 87 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 29 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 36 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 47 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 57 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 71 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–18
- **Visible Samples:** 19

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–40
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 40 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 126 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 186 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 239 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–20 | 21 | 1 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 3–239 | 189 | 5 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 33–83 | 47 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 34–99 | 38 | 3 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 70–239 | 170 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 79–239 | 94 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 94–239 | 146 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 134–172 | 39 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 139–140 | 2 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 141–223 | 79 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 142–143 | 2 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 145–239 | 88 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 158–239 | 82 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 168–239 | 38 | 3 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 180–239 | 59 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 197–203 | 4 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 201–208 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_BallSnap' at frame 12 targets track ID '[?]', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 159: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PassBlock' range [15-88] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-212] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-63] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-115] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-152] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-126] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-186] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-87] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-226] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-46] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [47-72] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [74-131] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [172-239] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-234] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-29] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-36] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-47] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-57] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-71] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-40] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-12] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-64] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-146] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-168] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-58] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-39] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-69] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-99] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-140] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-167] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-223] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-143] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-160] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-208] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-194] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-226] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-206] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-198] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-203] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-202] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-208] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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