# Play-Annotation-Generator Annotation Review — CrackToss_40

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_40`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 1
- **Action Segments:** 61
- **Validation Warnings:** 70
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 4
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `19` | `18` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Toss` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | SAF | defense | `8` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 56 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 57 | START | 57 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | `19` | `18` | 60 | START | 60 | 154 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `3` | `2` | 60 | START | 60 | 175 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 68 | END | 57 | 68 |
| ✅ EXACT | `Action_Toss` | QB | `7` | `6` | 71 | START | 71 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | SAF | `8` | `7` | 89 | START | 89 | 152 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_SnapReceive` | 57 | 68 | 12 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_Toss` | 71 | 88 | 18 | inferred_complete_timeline |
| `Action_None` | 89 | 123 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 161 | 105 | inferred_complete_timeline |
| `Action_None` | 166 | 174 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 175 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_BallSnap` | 57 | 68 | 12 | inferred_complete_timeline |
| `Action_None` | 69 | 116 | 48 | inferred_complete_timeline |
| `Action_None` | 121 | 156 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 153 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 175 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 175 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 105 | 49 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 104 | 48 | inferred_complete_timeline |
| `Action_None` | 111 | 175 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 146 | 90 | inferred_complete_timeline |
| `Action_None` | 156 | 175 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 175 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 175 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 81 | 25 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_BallCarry` | 89 | 152 | 64 | inferred_complete_timeline |
| `Action_BallCarry` | 154 | 157 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 159 | 175 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–175 | 176 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–166 | 167 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–175 | 174 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 18–159 | 141 | 3 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 82–83 | 2 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 92–175 | 81 | 2 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 117–175 | 59 | 1 | Undefined position; Undefined team |
| `22` | `32` | Position_Unknown | Team_Unknown | 119–142 | 24 | 1 | Undefined position; Undefined team |
| `23` | `35` | Position_Unknown | Team_Unknown | 135–175 | 41 | 1 | Undefined position; Undefined team |
| `24` | `38` | Position_Unknown | Team_Unknown | 151–175 | 25 | 1 | Undefined position; Undefined team |
| `25` | `39` | Position_Unknown | Team_Unknown | 159–166 | 8 | 1 | Undefined position; Undefined team |
| `26` | `41` | Position_Unknown | Team_Unknown | 162–174 | 6 | 2 | Undefined position; Undefined team |
| `27` | `42` | Position_Unknown | Team_Unknown | 169–171 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | 0 | 43 | 18 | 40.9% | 7–8, 13, 16–20, 23–30, 32–41 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 116 targets track ID '145', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 39 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 82: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 82: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 82: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '2' (Unknown) duration 116 frames exceeds threshold 90 frames [start=60, end=175].
- ⚠️ Action 'Action_None' range [57-153] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-161] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-174] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [60-175] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-175] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-81] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-146] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-175] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-123] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [89-152] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [154-157] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [159-175] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-175] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-156] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-105] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-175] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-104] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-175] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-175] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-166] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-175] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [60-154] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [156-159] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-142] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-175] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-175] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-175] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-166] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>